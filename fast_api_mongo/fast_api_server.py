import wmi
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'About'}

if __name__ == '__main__':
    # Getting the computer's unique ID
    # can be achieved through running in cmd "wmic DISKDRIVE get SerialNumber"
    c = wmi.WMI()
    hddSerialNumber = c.Win32_PhysicalMedia()[0].wmi_property('SerialNumber').value.strip()
    # print(hddSerialNumber)
