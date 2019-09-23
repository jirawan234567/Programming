#!/usr/bin/env python
# coding: utf-8

# 1.กำหนดให้ brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
# 
# 1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo
# 1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล
# 1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบมียี่ห้อรถ Suzuki, Ferrari, Ford อยู่ใน cars หรือไม่

# In[1]:


brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("รุ่นรถของยี่ห้อรถ คือ",brand_cars.index("Benz"))
print("รุ่นรถของยี่ห้อรถ Ford คือ",brand_cars.index("Ford"))
print("รุ่นรถของยี่ห้อรถ Volvo คือ",brand_cars.index("Volvo"))
print("จำนวนข้อมูลทั้งหมดในทูเพิล คือ",len(brand_cars),"รายการ")
print("โลโก้ Suzuki อยู่ใน brand_cars หรือไม่ =","Suzuki" in brand_cars)
print("โลโก้ Ferrari อยู่ใน brand_cars หรือไม่ =","Ferrari" in brand_cars)
print("โลโก้ Ford อยู่ใน brand_cars หรือไม่ =","Ford" in brand_cars)


# In[ ]:




