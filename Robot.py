from hub import port
import motor
import runloop
import motor_pair
import color_sensor
import color

def detected_color():
    return color_sensor.color(port.B) == color.BLACK

def color_detected():
    return color_sensor.color(port.B) == color.RED


async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.F, port.D)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=50000)

    await runloop.until(detected_color)
    if detected_color:
        motor.run_for_degrees(port.D, 9000, 18000)
    await runloop.until(color_detected)
    if color_detected:
        motor.run_for_degrees(port.F, 18000, 18000)

    
    

runloop.run(main())
