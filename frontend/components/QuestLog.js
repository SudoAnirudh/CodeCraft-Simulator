import React, { useEffect, useState } from 'react';

const QuestLog = () => {
    const [quests, setQuests] = useState([]);

    useEffect(() => {
        const fetchQuests = async () => {
            const response = await fetch('/api/quests');
            const data = await response.json();
            setQuests(data);
        };
        fetchQuests();
    }, []);

    return (
        <div className="quest-log">
            <h2>Quest Log</h2>
            <ul>
                {quests.map((quest) => (
                    <li key={quest.id}>{quest.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default QuestLog;
