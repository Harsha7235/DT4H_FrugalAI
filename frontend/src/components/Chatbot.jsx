import { useState } from "react";
import axios from "axios";

function Chatbot() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");

  const sendMessage = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat", {
      text: message,
    });
    setReply(res.data.reply);
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h2>Medical Chatbot</h2>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={sendMessage}>Send</button>
      <p>{reply}</p>
    </div>
  );
}

export default Chatbot;