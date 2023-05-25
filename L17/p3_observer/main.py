from L17.p3_observer.sensor import Sensor
from L17.p3_observer.subscribers import MobileApp, WebApp, AirConditioneer

sensor = Sensor()
mobile_app = MobileApp()
web_app = WebApp()
air_cond = AirConditioneer(17, 25)

sensor.subscribe(mobile_app)
sensor.subscribe(web_app)
sensor.subscribe(air_cond)

sensor.notify_all()
print()

sensor.unsubscribe(web_app)
sensor.notify_all()
print()

sensor.notify(mobile_app)



