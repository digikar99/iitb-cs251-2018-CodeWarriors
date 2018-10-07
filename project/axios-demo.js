// import React;
// import ReactDOM from 'react-dom';
// import axios from 'axios';



class FetchDemo extends React.Component {
	state = {
		textString: ''
	}

	getInitialState() {
		return {textString: '' }
	}

	componentDidMount() {
		axios.get(`http://127.0.0.1:8000/files_ud/`)
			.then((response) => {
				console.log(response.data);
			    this.setState({textString: response.data});
			});
	}

	render() {
		return (
				<div>
			    <h1>Received data:</h1>
				<p>{this.state.textString}</p>
			    </div>
		);
	}
}

ReactDOM.render(<FetchDemo/>,document.getElementById('root')); 
