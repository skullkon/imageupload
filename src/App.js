import React from 'react'
import LeftSide from './components/firstLab/LeftSide';
import RightSide from './components/secondLab/RightSide';
import './index.css'

function App() {
  return (
    <div>
      <div className="first">
        <LeftSide />
      </div>
      <div className="second">
        <RightSide />
      </div>
    </div >
  );
}

export default App;
