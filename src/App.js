import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './index.css'
import Signup from './api/Signup';
import Login from './api/Login';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path = 'signup/' Component={Signup} />
        <Route exact path = 'login/' Component={Login} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
