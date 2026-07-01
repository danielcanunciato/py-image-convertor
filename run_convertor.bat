@echo off

@IF NOT EXIST Images mkdir Images

title Image Convertor.py
color 1

echo Starting imageconvertorpy...
py image_convertor.py

echo Converted successfully, check Images folder.