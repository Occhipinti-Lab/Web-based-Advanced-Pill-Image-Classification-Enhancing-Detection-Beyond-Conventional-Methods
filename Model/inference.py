from fastai.vision import *




learn = load_learner('models_pile_densnet')







def get_result(img_path):
    cls, ss, d = learn.predict(open_image(img_path))
    print(cls, int(ss))
    return cls


impath='3B-Medi_20210324_205358569627-7.jpg'
get_result(impath)
