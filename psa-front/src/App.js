import './App.css';
import TabNavigator from './components/TabNavigator';
import ProyectosScreen from './tabsContents/Proyectos';
import SoporteScreen from './tabsContents/Soporte';
import RecursosScreen from './tabsContents/Recursos';


function App() {
  return (
    <div className="App">
      <header>
        <div>PSA</div>
      </header>
      <body>
        <TabNavigator 
          tabs={['Proyectos', 'Soporte', 'Recursos']}
          contents={[<ProyectosScreen/>, <SoporteScreen/>, <RecursosScreen/>]}
        />
      </body>
    </div>
  );
}

export default App;
