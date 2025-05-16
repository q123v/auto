basic.forever(function () {
    if (15 >= maqueen.Ultrasonic()) {
        maqueen.motorStop(maqueen.Motors.All)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 90)
    } else {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 35)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 35)
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 35)
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 35)
            }
        } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 35)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 35)
            }
            if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
                maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 35)
            } else {
                maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            }
        }
    }
})
basic.forever(function () {
	
})
