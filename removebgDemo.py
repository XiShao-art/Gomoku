from removebg import RemoveBg as rb
import os

rmbg = rb("WPZ2Q4fraseKfANPPxxxxxx", "error.log")
path = 'D:\study\我\登记照\登记照18.jpg'
rmbg.remove_background_from_img_file(path)
rmbg.remove_background_fr