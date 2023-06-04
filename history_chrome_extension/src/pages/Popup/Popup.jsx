import React from 'react';
import logo from '../../assets/img/logo2.svg';
import './Popup.css';

const Popup = () => {
  const handleSearchHistory = () => {
    chrome.history.search({ text: '', startTime: 0, maxResults: 200 }, function(data) {
      let urls = data.map(page => page.url); // URLのリストを取得
      let titles = data.map(page => page.title); // URLのリストを取得
      console.log('URLs:', urls); // URLのリストをコンソールに出力

      let endpoint = 'http://127.0.0.1:8000/history/';
      let data_ = { urls: urls , titles: titles}; // リクエストのデータとしてURLのリストを使用
      
      postData(endpoint, data_);

      var url = "https://example.com"; // 遷移先の URL を指定する
      window.open(url, "_blank");

    });
  };

const postData = (url, data) => {
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

  return (
    <div className="App">
      <header className="App-header">
        <h1>Chrome History Extension</h1>
        <img src={logo} className="App-logo" alt="logo" />
        <p></p>
        <button id='postButton' onClick={handleSearchHistory}>POST History Data</button>
        <p></p>
      </header>
    </div>
  );
};

export default Popup;
