import React, { useState } from 'react';

const CodeEditor = () => {
    const [code, setCode] = useState('');
    const [output, setOutput] = useState('');

    const handleRunCode = async () => {
        const response = await fetch('/api/submit_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: 1, code })
        });
        const result = await response.json();
        setOutput(result.output || result.error);
    };

    return (
        <div className="code-editor">
            <h2>Code Editor</h2>
            <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                rows="10"
                cols="50"
            ></textarea>
            <button onClick={handleRunCode}>Run Code</button>
            <pre>{output}</pre>
        </div>
    );
};

export default CodeEditor;
