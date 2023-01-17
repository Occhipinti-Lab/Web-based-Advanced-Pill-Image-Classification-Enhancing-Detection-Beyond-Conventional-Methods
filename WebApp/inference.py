from fastai.vision import *




learn = load_learner('static/models_pile_densnet')







def get_result(img_path):
    flage = False
    cls =''
    try:
        cls, ss, d = learn.predict(open_image(img_path))
        print(cls, int(ss))
        flage = True

    except:
        pass

    return flage, cls




# get_result()

