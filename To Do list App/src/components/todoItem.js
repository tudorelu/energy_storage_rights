import React from 'react';
import './todoItem.css';

export default class TodoItem extends React.Component{
    constructor(props){
        super(props);
    }

    deleteTodo(id){
        this.props.deleteTodo(id);
    }


    render(){
        return(
            <div className="todoWrapper">
                <button className="btn btn-primary" onClick={() => this.deleteTodo(this.props.todo.id)}>Delete</button>
                {this.props.todo.text}
            </div>
        )
    }
}