#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    result = (a+b+c)/3
    
    return result 


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_radian = angle_degs+(angle_mins+angle_secs/60)/60
    angle_radian_final = angle_radian*(math.pi/180)
    
    return angle_radian_final


def to_degrees(angle_rads: float) -> tuple:
    angle_en_degree = angle_rads*180/math.pi
    angle_degree = angle_en_degree
    angle_min = angle_en_degree*60
    angle_sec = angle_en_degree*3600
    
    return angle_degree,angle_min,angle_sec 


def to_celsius(temperature: float) -> float:
    temperature_celsius = (temperature/1.8)-32
    
    return temperature_celsius


def to_farenheit(temperature: float) -> float:
    temperature_farenheit = (temperature*1.8)+32
    
    return temperature_farenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
