from flask_restful import Resource,Api,reqparse,abort,fields,marshal
from flask import  Flask

#use Flask-RESTful to design RESTful API


app=Flask(__name__)
api=Api(app,prefix='/index/api')

tasks = [
    {'id':          1,
     'title':      'task1',
     'description': 'a good movie'

     },
    {'id':          2,
     'title':       'task2',
     'description': 'a bad movie'
     }
]

def if_exists_id(id):
    task=list(filter(lambda x:x['id']==id,tasks))
    assert len(task) > 0, abort(404, errors='not found')
    return task[0]


class TasksApi(Resource):

    def __init__(self):
        self.reparse = reqparse.RequestParser()
        self.reparse.add_argument('title', type=str,required=True,help='check title!')
        self.reparse.add_argument('description',type=str,default='')


    def get(self):
        return {'tasks':tasks},200
    # curl  http://127.0.0.1:5000/index/api/tasks
    def post(self):
        args=self.reparse.parse_args(strict=True)
        args.setdefault('id', tasks[-1]['id'] + 1)
        tasks.append(args)
        return {'task':args},201
    #curl -i -X POST -d 'title=task3' http://127.0.0.1:5000/index/api/tasks


class TaskApi(TasksApi):
    taskFiled={
        'id':fields.Integer,
        'title':fields.String,
        'description':fields.String,
        'uri':fields.Url('taskapi')
    }
    def __init__(self):
        super(TaskApi,self).__init__()
        self.reparse.args[0].required=False#modify title required

    def get(self,id):
        task=if_exists_id(id)
        return {'task':marshal(task,TaskApi.taskFiled)},200

    # curl -i  http://127.0.0.1:5000/index/api/tasks/1

    def put(self,id):
        task=if_exists_id(id)
        args=self.reparse.parse_args(strict=True)
        task['title']=args.get('title') or task['title']
        task['description']=args.get('description') or task['description']

        return {'task': marshal(task, TaskApi.taskFiled)}, 200
    #curl -i -X PUT -d 'description= dog dog' http://127.0.0.1:5000/index/api/tasks/1


api.add_resource(TasksApi,'/tasks')
api.add_resource(TaskApi,'/tasks/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)