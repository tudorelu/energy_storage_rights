import React, { Component } from 'react';
import Header from './components/header';
import './App.css';
import TodoInput from './components/todoInput';
import TodoItem from './components/todoItem';

class App extends Component {
  constructor(props){
    super(props);

    this.state = {
      todos: [
        {id : 0, text :"👈this button deletes only one single todo thing"},
        {id : 1, text: "this button deletes all todo things👇"}
      ],
      nextId: 2
    
    }

    this.addTodo = this.addTodo.bind(this);
    this.deleteTodo = this.deleteTodo.bind(this);
  }

  addTodo(todoText){
    let todos = this.state.todos.slice();
    let currId = this.state.nextId;
    todos.push({id: currId, text: todoText});
    this.setState({
      todos: todos,
      nextId: ++this.state.nextId
    });
  }

  deletAll(){
    this.setState({todos: []});
  }

  deleteTodo(id){
    let tempTodo = this.state.todos.slice();
    let result = [];
    for ( var i = 0; i < tempTodo.length; i++ ) {
      if (tempTodo[i].id != id) {
        result.push(tempTodo[i]);
      }
    }
    this.setState({todos : result});
    console.log("Called delete on "+id);
    
  }

  render() {
    return (
      <div className="App">
        <div className="todo-wrpper">
          <Header />
          <TodoInput todoText="" addTodo={this.addTodo}/>
          <ul>
            {
              this.state.todos.map((todo) => {
                return <TodoItem todo={todo} key={todo.id} deleteTodo={this.deleteTodo}/>
              })
            }
          </ul>
        </div>
        <div>
          <button className="btn btn-primary" onClick={() => this.deletAll()} >deletAll</button>
        </div>
      </div>
    );
  }
}

export default App;
