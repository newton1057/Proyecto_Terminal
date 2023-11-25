import './App.css';
import GraphView from './Components/Graph';
import Logo from './Images/Logo_White.png';

function App() {
  return (
    <div className="App">
      <div>
        <img src={Logo} alt='' style={{width: '200px'}}/>
      </div>
      <GraphView />
      
    </div>
  );
}

export default App;
