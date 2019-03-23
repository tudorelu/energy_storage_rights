import React from 'react';
import './todoInput.css';


export default class TodoInput extends React.Component{
    constructor(props){
        super(props);

        this.state = {value: 'this button is to add a new todo thing to the todo list👉'};

        this.handleChange = this.handleChange.bind(this);
        this.addTodo = this.addTodo.bind(this);

    }

     handleChange(e){
         this.setState({value: e.target.value});
     }

     addTodo(todo){
         if (todo.length > 0) {
            this.props.addTodo(todo);
            this.setState({value:''}); 
         }
         
     }


    render(){
        return(
          
            <div>
                <input type="text" value={this.state.value} onChange={this.handleChange} />
                <button className="btn btn-in" onClick={() => this.addTodo(this.state.value)}>AddToList</button>
            </div>
      
            
        );
    }

    




}