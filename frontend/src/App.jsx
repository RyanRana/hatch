import React from 'react';
import ResumeUpload from './components/ResumeUpload';
import SearchForm from './components/SearchForm';
import JobResults from './components/JobResults';

function App() {
  return (
    <div className='p-4'>
      <h1 className='text-2xl font-bold'>Hatch Job Discovery</h1>
      <ResumeUpload />
      <SearchForm />
      <JobResults />
    </div>
  );
}

export default App;