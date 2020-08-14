from PIL import Image
from threading import Thread
import os.path

class MyValidate(object):

    def __init__(self, data=None, validators=None):
        self.data = data
        self.errors = []
        self.check_validators(validators)
        self.validators = validators
        self.success=False

    def validate(self):
        for validator in self.validators:
            try:
                validator(self)
            except IOError as e:
                self.errorrs.append(e)
            except Exception as e:
                self.errors.append(e)
        if not len(self.errors):
            self.success=True

        return self.success




    @classmethod
    def check_validators(cls, validators):
        if validators:
            assert '__getitem__' in dir(validators), 'validators should be a list or tuple'
            for validator in validators:
                if not callable(validator):
                    raise TypeError('{} should be callable!'.format(validator))




        # def strip(data):
    #     print type(data),repr(data),__name__
    #     if data is None:
    #         return
    #     if not data.strip():
    #         raise ValueError('Invalid input!')
    #     return data
    # def run_validate(self,validator=()):

class ImageVlidator(object):

    def __init__(self,filename,save_path,name='ImageVlidator'):
        self.name=name
        self.filename=filename
        self.save_path=save_path

    def __call__(self,MyValidate,*args,**kwargs):
        if not MyValidate.data:
            return
        try:
            image = Image.open(MyValidate.data)
        except IOError as e:
            raise IOError(e.args)

        Image_Format = ('JPEG', 'PNG')
        if image.format not in Image_Format:
            raise ValueError("Not support %s format,please use jpeg,png" % (image.format))


        if image.height < 200 or image.width < 200 or image.height > 5000 or image.width > 5000:
            raise ValueError('width and length of image should be bigger 200,and less than 5000')

        image.thumbnail(size=(200, 200))

        MyValidate.filename = self.filename +'.'+image.format.lower()

        try:
            ret=Thread(target=image.save,args=[os.path.join(self.save_path, MyValidate.filename)])
            ret.start()
            MyValidate.success=True
        except Exception as e:
            raise Exception(e)



    def __str__(self):
        return self.name






