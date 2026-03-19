import logo from '../public/logo192.png';
import './App.css';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="OctoFit Logo" />
        <div style={{ marginLeft: 80 }}>
          <h1 className="mb-3">OctoFit Tracker</h1>
          <nav className="navbar navbar-expand navbar-light">
            <a className="navbar-brand" href="#">Home</a>
            <ul className="navbar-nav">
              <li className="nav-item"><a className="nav-link" href="#users">Users</a></li>
              <li className="nav-item"><a className="nav-link" href="#teams">Teams</a></li>
              <li className="nav-item"><a className="nav-link" href="#activities">Activities</a></li>
              <li className="nav-item"><a className="nav-link" href="#leaderboard">Leaderboard</a></li>
              <li className="nav-item"><a className="nav-link" href="#workouts">Workouts</a></li>
            </ul>
          </nav>
        </div>
      </header>
      <main className="container mt-5">
        <div className="card">
          <div className="card-header">Welcome to OctoFit Tracker!</div>
          <div className="card-body">
            <p className="card-text">Track your fitness activities, join teams, and climb the leaderboard. Use the navigation menu to explore features.</p>
            <a href="#activities" className="btn btn-primary">Get Started</a>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
