const axios = require('axios');

const baseURL = 'http://localhost:8000/history/'
const userId = 1

const extractHostname = (url) => {
    const parsedUrl = new URL(url);
    return parsedUrl.hostname;
};

// 一意のhostnameのリストを作成，REST APIのエンドポイントにpost
const postUniqueHostnames = async (urls) => {
    const uniqueHostnames = [...new Set(urls.map(url => extractHostname(url)))];
    const data = uniqueHostnames.map(hostname => ({ "hostname": hostname }));
    const json_data = JSON.stringify(data)
    console.log(json_data);

    try {
        await axios.post(baseURL + 'host/', data);
        console.log('Unique hostnames data sent successfully');
    } catch (error) {
        // console.log('Failed to send unique hostnames data:', error);
        console.log(json_data);
  }
};

// URLに関するデータをREST APIのエンドポイントにpost
const postUrls = async (urls, titles) => {
    const data = urls.map((url, index) => ({
        url,
        title: titles[index],
        host: extractHostname(url)
    }));
    const json_data = JSON.stringify(data)
    console.log(json_data);

    try {
        await axios.post(baseURL + 'url/', data);
        console.log('URL data sent successfully');
    } catch (error) {
        // console.log('Failed to send URL data:', error);
        console.log(json_data);

    }
};


const postBrowsingHistories = async (urls, userId) => {
  const data = urls.map(url => ({
    url,
    user: userId
  }));
  console.log(JSON.stringify(data));

  try {
    await axios.post(baseURL + userId + '/', data);
    console.log('Browsing history data sent successfully');
  } catch (error) {
    // console.log('Failed to send browsing history data:', error);
    console.log(json_data);
  }
};

// 使用例
const urls = [
    'https://www.example1.com/page1',
    'https://www.example2.com/page2',
    'https://www.example3.com/page3'
];

const titles = [
    'Page 1',
    'Page 2',
    'Page 3'
];

postUniqueHostnames(urls);
postUrls(urls, titles);
postBrowsingHistories(urls, userId);
