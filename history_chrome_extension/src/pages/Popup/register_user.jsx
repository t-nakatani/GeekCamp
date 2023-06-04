export const registerUser = (username) => {
    const url = 'http://example.com/api/register';
    const data = { username: username };
  
    return fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Failed to register user');
      }
    })
    .then(responseData => {
      const userId = responseData.userId;
      localStorage.setItem('userId', userId);
    })
    .catch(error => {
      console.log('Error:', error);
    });
  };
  
  export const getUserId = () => {
    const userId = localStorage.getItem('userId');
    return userId;
  };
  