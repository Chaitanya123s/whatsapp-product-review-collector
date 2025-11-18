import React, { useEffect, useState } from 'react';

function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch('/api/reviews')
      .then(res => res.json())
      .then(setReviews)
      .catch(console.error);
  }, []);

  return (
    <div style={{padding: 24, fontFamily: 'Arial'}}>
      <h1>Product Reviews (WhatsApp)</h1>
      <table style={{width: '100%', borderCollapse: 'collapse'}}>
        <thead>
          <tr>
            <th style={{textAlign: 'left', padding: 8}}>User</th>
            <th style={{textAlign: 'left', padding: 8}}>Product</th>
            <th style={{textAlign: 'left', padding: 8}}>Review</th>
            <th style={{textAlign: 'left', padding: 8}}>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map(r => (
            <tr key={r.id} style={{borderTop: '1px solid #ddd'}}>
              <td style={{padding: 8}}>{r.user_name || r.contact_number}</td>
              <td style={{padding: 8}}>{r.product_name}</td>
              <td style={{padding: 8}}>{r.product_review}</td>
              <td style={{padding: 8}}>{new Date(r.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <p style={{marginTop: 20}}>Messages are collected via Twilio WhatsApp Sandbox and saved into Postgres.</p>
    </div>
  );
}

export default App;
