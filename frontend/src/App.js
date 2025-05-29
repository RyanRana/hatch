import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [resume, setResume] = useState(null);
  const [term, setTerm] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const form = new FormData();
    form.append('resume_file', resume);
    form.append('search_term', term);
    const res = await axios.post('http://localhost:8000/match', form);
    setResults(res.data);
  };

  return (
    <div className="p-10 max-w-2xl mx-auto font-sans">
      <h1 className="text-4xl font-bold mb-6 text-center">🚀 Hatch</h1>
      <p className="mb-4 text-center text-gray-600">Upload your resume. Enter your goal. We'll hatch the best jobs for you.</p>
      <input type="file" onChange={e => setResume(e.target.files[0])} className="w-full mb-4" />
      <input onChange={e => setTerm(e.target.value)} placeholder="e.g. React Developer Remote" className="w-full p-2 border mb-4" />
      <button onClick={handleSearch} className="bg-indigo-600 text-white px-4 py-2 rounded w-full">🔍 Find Jobs</button>
      <div className="mt-6">
        {results.map((r, i) => (
          <div key={i} className="border p-4 mb-4 rounded shadow-sm">
            <h2 className="text-xl font-semibold">{r.job.title}</h2>
            <p className="text-gray-700">{r.job.description}</p>
            <a href={r.job.url} className="text-blue-600 underline" target="_blank" rel="noopener noreferrer">View Job</a>
            <p className="text-sm text-gray-500">Match Score: {(r.score * 100).toFixed(2)}%</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
