import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar'
import LandingPage from './components/LandingPage'
import ServiceLvl from './components/ServiceLvl'
import PopularProducts from './components/PopularProducts'
import Footer from './components/Footer'

function App() {
  return (
    <>
      <Navbar/>
      <LandingPage/>
      <ServiceLvl/>
      <PopularProducts/>
      <Footer/>
    </>
  );
}

export default App;
