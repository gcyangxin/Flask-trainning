from flask import  Flask,jsonify,abort,make_response,request

#use Python and Flask to design RESTful API

app=Flask(__name__)

tasks = [
    {'id':          1,
     'titele':      'HERO',
     'description': ' good movie'

     },
    {'id':          2,
     'title':       'wuji',
     'description': 'bad movie'
     }
]

@app.errorhandler(404)
def not_found(error):
    return  make_response(jsonify({'error':'not found'}),404)

@app.route('/index/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

#$ curl -i http://127.0.0.1:5000/index/api/tasks


@app.route('/index/api/tasks/<int:task_id>')
def get_task(task_id):

    task=list(filter(lambda x:x['id']==task_id,tasks))
    assert len(task)>0,abort(404)
    return jsonify(task=task[0])
#$ curl -i http://127.0.0.1:5000/index/api/tasks/1


@app.route('/index/api/tasks',methods=['POST'])
def create_task():
    print (request.json)
    if not request.json or not 'title'  in request.json:
        abort(400)
    task={'id':          tasks[-1]['id']+1,
     'titele':      request.json['title'],
     'description': request.json.get('description','')
     }
    tasks.append(task)
    return jsonify({'task':task}),201
#$ curl -i -H 'Content-Type: application/json' -X POST -d '{"title":"mylove"}' http://127.0.0.1:5000/index/api/tasks

@app.route('/index/api/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    if not request.json:
        abort(400)
    task=list(filter(lambda x:x['id']==task_id,tasks))
    assert len(task)>0,404
    task=task[0]
    if request.json.get('title'):
        task['title']=request.json.get('title')
    if request.json.get('decription'):
        task['decription'] = request.json.get('decription')


    return jsonify({'task':task})
#curl -i -H 'Content-Type: application/json' -X PUT -d '{"title":"mylove1","decription":"googgoog"}' http://127.0.0.1:5000/index/api/tasks/2


@app.route('/index/api/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    task=list(filter(lambda x:x['id']==task_id,tasks))
    assert len(task)>0,404

    tasks.remove(task[0])
    return jsonify({'result':True})
#curl -i -X DELETE  http://127.0.0.1:5000/index/api/tasks/2

if __name__ == '__main__':
    app.run(debug=True)