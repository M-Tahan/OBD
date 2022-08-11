import obd
connection = obd.OBD('/dev/ttyUSB0')
intSpeed = ""
class OBDvar():
    
    def speedResults():
        cmd_speed = obd.commands.SPEED
        speed_response = connection.query(cmd_speed)
        speedR = speed_response.value
        strSpeed = str(speedR)
        
        for i in range(len(strSpeed)):
            if(strSpeed[i] == "."):
                break
            else:
                intSpeed = intSpeed + strSpeed[i]

        return(int(intSpeed))
    
    def rpmResults():
        cmd_rpm = obd.commands.RPM
        rpm_response = connection.query(cmd_rpm)
        rpmR = rpm_response.value
        strRPM = str(rpmR)
        
        for i in range(len(strRPM)):
            if(strRPM[i] == "."):
                break
            else:
                intRPM = intRPM + strRPM[i]

        return(int(intRPM))
