import React from 'react';
import ReactDOM from 'react-dom';
import CodeEditor from './components/CodeEditor';
import CityView from './components/CityView';
import QuestLog from './components/QuestLog';
import Tutorial from './components/Tutorial';

const App = () => {
    return (
        <div className="container">
            <h1>CodeCraft Simulator</h1>
            <Tutorial />
            <CityView />
            <CodeEditor />
            <QuestLog />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('app'));
