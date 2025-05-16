def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    if 15 >= maqueen.ultrasonic():
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.motor_stop(maqueen.Motors.ALL)
    else:
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
basic.forever(on_forever)

def on_forever2():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 35)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 35)
    else:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 35)
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 35)
        else:
            if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
                maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 35)
                maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 35)
                if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
                    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 35)
                else:
                    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
basic.forever(on_forever2)
