//
//  PlanetarySystem.cpp
//
//  Created by Shoya DOZONO on 2017/10/26.
//
//

#include "PlanetarySystem.h"

PlanetarySystem::PlanetarySystem()
    : mMode(Mode::FOLLOW)
    , mScale(1)
    , mMaxNumPlanets(6)
    , mExapandSpeed(0.1)
    , mCamRotateSpeed(8.0)
    , mCamera(Camera::MANUAL)
    , mCamZoom(350)
    , mTrailOpacity(1.0)
    , mLineOpacity(0.0)
    , mLineMode(OF_PRIMITIVE_LINE_STRIP)
#ifdef USE_MOTIONER
    , mVelocityThreshold(2.5)
#else
    , mVelocityThreshold(0.25)
#endif
{;}

void PlanetarySystem::setup()
{
    mTargets.push_back(rdtk::Actor::JOINT_LEFT_HAND);
    mTargets.push_back(rdtk::Actor::JOINT_RIGHT_HAND);
    mTargets.push_back(rdtk::Actor::JOINT_LEFT_ANKLE);
    mTargets.push_back(rdtk::Actor::JOINT_RIGHT_ANKLE);
    mTargets.push_back(rdtk::Actor::JOINT_HEAD);
    
    mVelocityManagers.resize(mTargets.size());
    
    // setup osc
    mOscReceiver.setup(8888);
}

void PlanetarySystem::update()
{
    while ( mOscReceiver.hasWaitingMessages() )
    {
        ofxOscMessage m;
        mOscReceiver.getNextMessage(m);
        ofLog() << m.getAddress();
        
        if ( m.getAddress() == "/trail_opacity" )
        {
            mTrailOpacity = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/line_opacity" )
        {
            mLineOpacity = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/mode" )
        {
            int mode = m.getArgAsInt(0);
            if ( mode == 0 ) mMode = Mode::STABLE;
            if ( mode == 1 ) mMode = Mode::FOLLOW;
            if ( mode == 2 ) mMode = Mode::PARTS;
            this->reset();
        }
        
        if ( m.getAddress() == "/camera" )
        {
            int camera = m.getArgAsInt(0);
            if ( camera == 0 ) mCamera = Camera::MANUAL;
            if ( camera == 1 ) mCamera = Camera::ROTATION;
            if ( camera == 2 ) mCamera = Camera::FOLLOW;
        }
        
        if ( m.getAddress() == "/line_mode" )
        {
            int lineMode = m.getArgAsInt(0);
            if ( lineMode == 0 ) mLineMode = OF_PRIMITIVE_LINE_STRIP;
            if ( lineMode == 1 ) mLineMode = OF_PRIMITIVE_LINE_LOOP;
        }
        
        if ( m.getAddress() == "/max_num_planets" )
        {
            mMaxNumPlanets = m.getArgAsInt(0);
        }
        
        if ( m.getAddress() == "/scale" )
        {
            mScale = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/expand_speed" )
        {
            mExapandSpeed = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/velocity_threshold" )
        {
            mVelocityThreshold = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/cam_rotate_speed" )
        {
            mCamRotateSpeed = m.getArgAsFloat(0);
        }
        
        if ( m.getAddress() == "/cam_zoom" )
        {
            mCamZoom = m.getArgAsFloat(0);
        }
        
    }
    
    
    for ( auto it = mPlanets.begin(); it != mPlanets.end(); )
    {
        if ( !(*it)->isAlive() ) it = mPlanets.erase(it);
        else ++it;
    }
}

void PlanetarySystem::draw()
{
    // rotate camera
    if ( mCamera == Camera::ROTATION )
    {
        rdtk::BeginCamera();
        {
            auto & cam = rdtk::CameraManager::instance().getActiveCamera();
            cam.orbit(ofGetElapsedTimef() * mCamRotateSpeed, -30.0, mCamZoom);
        }
        rdtk::EndCamera();
    }
    
    // draw helpers1
    if ( mShowHelpers )
    {
        stringstream ss;
        for ( int i=0; i < mVelocityManagers.size(); i++)
        {
            ss << mTargets[i] << ": " << ofToString(mVelocityManagers[i].getAverage().length(), 2) << "\n";
        }
        ofPushStyle();
        ofSetColor(255);
        ofDrawBitmapString(ss.str(), 20, 20);
        ofPopStyle();
    }
}

void PlanetarySystem::drawPlanet(const rdtk::NodeArray &nodeArray)
{
    static uint64_t lastAddedPlanetTimeMillis = 0;
    
    for (int i=0; i < mTargets.size(); i++)
    {
        auto n = nodeArray.getNode(mTargets[i]);
        mVelocityManagers[i].setVelocity(n.getVelocity());
        if ( mVelocityManagers[i].update() )
        {
            if ( mVelocityManagers[i].getAverage().length() > mVelocityThreshold )
            {
                if ( mPlanets.size() < mMaxNumPlanets && ofGetElapsedTimeMillis() - lastAddedPlanetTimeMillis > 2000 )
                {
                    auto planet = this->addPlanet();
                    planet->joint(i);
                    planet->speed(0.002);
                    planet->radius(0);
                    planet->rotate(ofVec3f(0.0, ofRandom(-120.0, 120.0), ofRandom(-120.0, 120.0)));
                    planet->rotateSpeed(ofVec3f(0.0, ofRandom(-0.05, 0.05), ofRandom(-0.05, 0.05)));
                    
                    if ( mMode == Mode::PARTS )
                    {
                        planet->center(n.getGlobalPosition());
                    }
                    
                    lastAddedPlanetTimeMillis = ofGetElapsedTimeMillis();
                }
            }
        }
        
    }
    
    for ( auto &planet : mPlanets )
    {
        if ( mMode == Mode::FOLLOW ) {
            planet->center(nodeArray.getNode(rdtk::Actor::JOINT_ABDOMEN));
        }
        else if ( mMode == Mode::STABLE ) {
            planet->center(ofVec3f(0, 100, 0));
        }
        
        if ( planet->getJoint() >= 0 )
        {
            if ( mVelocityManagers[planet->getJoint()].isComputeAverage() )
            {
                auto vel = mVelocityManagers[planet->getJoint()].getAverage().length();
#ifdef USE_MOTIONER
                planet->speed(vel * 0.002);
#else
                planet->speed(vel * 0.05 + 0.0001);
#endif
            }
        }
        
        planet->scale(mScale);
        planet->expandSpeed(mExapandSpeed);
        planet->update();
        planet->color(ofColor::white);
        planet->drawPlanet();
        planet->drawTrail(mTrailOpacity);
    }
    
    ofPushStyle();
    ofSetColor(ofColor::white, 196.f * mLineOpacity);
    ofSetLineWidth(3.0);
    ofMesh mesh;
    mesh.setMode(mLineMode);
    for ( auto &planet : mPlanets )
    {
        mesh.addColor(ofFloatColor(1.0, 1.0, 1.0, 0.75 * planet->getOpacity() * mLineOpacity));
        mesh.addVertex(planet->getPoint());
    }
    mesh.draw();
    ofPopStyle();
    
    
    if ( mShowHelpers )
    {
        for (int i=0; i < mTargets.size(); i++)
        {
            auto n = nodeArray.getNode(mTargets[i]);
            auto average = mVelocityManagers[i].getAverage();
            
            ofPoint pt = n.getGlobalPosition();
            
            ofPushStyle();
            ofSetColor(rdtk::Color::BLUE_LIGHT);
            ofSetLineWidth(4.0);
            ofDrawLine(pt, pt + average * 1000.0);
            ofPopStyle();
        }
    }
}

ofPtr<Planet> PlanetarySystem::addPlanet()
{
    ofPtr<Planet> o = ofPtr<Planet>(new Planet);
    mPlanets.push_back(o);
    return o;
}

void PlanetarySystem::randomize()
{
    for ( auto &o : mPlanets )
    {
        o->speed(ofRandom(0.001, 0.003));
        o->radius(ofRandom(50, 350));
        o->rotate(ofVec3f(0.0, ofRandom(-60.0, 60.0), ofRandom(-60.0, 60.0)));
        o->rotateSpeed(ofVec3f(0.0, ofRandomuf() > 0.5 ? 0.01 : 0.0, ofRandomuf() > 0.5 ? 0.01 : 0.0));
    }
}

void PlanetarySystem::reset()
{
    mPlanets.clear();
}

void PlanetarySystem::drawActor(const rdtk::Actor& actor)
{
    if ( mCamera == Camera::FOLLOW )
    {
        rdtk::BeginCamera();
        {
            auto & cam = rdtk::CameraManager::instance().getActiveCamera();
            cam.orbit(ofGetElapsedTimef() * mCamRotateSpeed, -30.0, mCamZoom, actor.getNode(rdtk::Actor::JOINT_HEAD));
            cam.lookAt(actor.getNode(rdtk::Actor::JOINT_HEAD).getGlobalPosition());
        }
        rdtk::EndCamera();
    }
    
    this->drawPlanet(actor);
}

void PlanetarySystem::drawRigid(const rdtk::RigidBody &rigid)
{
    
}

void PlanetarySystem::drawImGui()
{
    if ( ImGui::Button("Reset") )
    {
        this->reset();
    }
    
    ImGui::SameLine();
    
    if ( ImGui::Button("Add Planet") )
    {
        auto planet = this->addPlanet();
        planet->speed(0.002);
        planet->radius(0);
        planet->rotate(ofVec3f(0.0, ofRandom(-120.0, 120.0), ofRandom(-120.0, 120.0)));
        planet->rotateSpeed(ofVec3f(0.0, ofRandom(-0.05, 0.05), ofRandom(-0.05, 0.05)));
    }
    
    ImGui::SameLine();
    
    if ( ImGui::Button("Randomize Parameters") )
    {
        this->randomize();
    }
    
    ImGui::NewLine();
    
    ImGui::Text("Num Planets: %d", (int)mPlanets.size());
    
    ImGui::NewLine();
    
    ImGui::SliderFloat("Trail Opacity", &mTrailOpacity, 0.0, 1.0);
    ImGui::SliderFloat("Line Opacity", &mLineOpacity, 0.0, 1.0);
    
    ImGui::NewLine();
    
    ImGui::Text("Planet Control");
    
    static int mode = 1;
    if ( ImGui::Combo("Mode", &mode, "STABLE\0FOLLOW\0PARTS\0\0") )
    {
        if ( mode == 0 ) mMode = Mode::STABLE;
        if ( mode == 1 ) mMode = Mode::FOLLOW;
        if ( mode == 2 ) mMode = Mode::PARTS;
        this->reset();
    }
    
    ImGui::SliderInt("Max Num Planets", &mMaxNumPlanets, 1, 10);
    
    ImGui::SliderFloat("Scale", &mScale, 0.0, 2.0);
    
    ImGui::SliderFloat("Expand Speed", &mExapandSpeed, 0.0, 1.0);
    
    ImGui::SliderFloat("Velocity Threshold", &mVelocityThreshold, 0.0, 3.0);
    
    static int lineMode = 0;
    if ( ImGui::Combo("Line Mode", &lineMode, "LINE_STRIP\0LINE_LOOP\0\0") )
    {
        if ( lineMode == 0 ) mLineMode = OF_PRIMITIVE_LINE_STRIP;
        if ( lineMode == 1 ) mLineMode = OF_PRIMITIVE_LINE_LOOP;
    }
    
    
    ImGui::NewLine();
    
    ImGui::Text("Camera Control");
    
    static int camera = 0;
    if ( ImGui::Combo("Camera Mode", &camera, "MANUAL\0ROTATION\0FOLLOW\0\0") )
    {
        if ( camera == 0 ) mCamera = Camera::MANUAL;
        if ( camera == 1 ) mCamera = Camera::ROTATION;
        if ( camera == 2 ) mCamera = Camera::FOLLOW;
    }
    
    ImGui::SliderFloat("Cam Rotate Speed", &mCamRotateSpeed, 0.0, 10.0);
    
    ImGui::SliderFloat("Cam Zoom", &mCamZoom, 100.0, 600.0);
    
    ImGui::NewLine();
    
    ImGui::Checkbox("Show Helpers", &mShowHelpers);
}
