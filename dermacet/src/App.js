import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar'
import LandingPage from './components/LandingPage'
import ServiceLvl from './components/ServiceLvl'
import PopularProducts from './components/PopularProducts'

function App() {
  return (
    <>
      <Navbar/>
      <LandingPage/>
      <ServiceLvl/>
      <PopularProducts/>
    </>
  );
}

export default App;
