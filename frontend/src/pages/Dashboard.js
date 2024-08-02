import React, { useState } from 'react';
import { Container, Grid, Button, TextField, CircularProgress, Paper, Typography, Avatar } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';
import { useTheme } from '@mui/material/styles';

import AiAvatar from '../components/AiAvatar';

import useLogout from '../hooks/Logout';
import useGenerateRuleEngine from '../hooks/GenerateRuleEngine';

import logoImage from '../media/logo.png';

import './Dashboard.css';

const Dashboard = () => {
    const theme = useTheme();
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const { logout } = useLogout();
    const { generateRuleEngine } = useGenerateRuleEngine();

    const EMPTY_CHAT_MESSAGE = `
        Platform is integrated and system is ready! You can now start
        creating your rule engine. Ask the AI agent to generate a rule
        and provide the necessary details.
    `;

    const handleInputChange = (event) => {
        setInput(event.target.value);
    };

    const handleSendMessage = () => {
        if (input.trim() !== '') {
            setIsLoading(true);
            setMessages([...messages, {"role": "user", "content": input}]);
            setInput('');

            const ruleEngineData = {
                user_prompt: input,
                chat_history: messages,
                integration_id: 0,
                is_generated: false
            };
            generateRuleEngine(ruleEngineData, setIsLoading, setMessages);
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSendMessage();
        }
    };

    return (
        <>
            <Grid container className="dashboard-container">
                <Grid item xs={12}>
                    <div className="navbar-static-top">
                      <div className="navbar-column-left">
                        <a href="/" className="navbar-brand" >
                            <img
                                src={logoImage}
                                alt="Smart Rule Engine Logo from logo.com"
                                className="dashboard-logo"
                            />
                        </a>
                      </div>

                      <div className="navbar-column-center">
                      </div>

                      <div className="navbar-column-right">  
                        <ul className="menu-items-list">
                            <li>
                                <a onClick={logout} className="link-button">
                                  Sign Out
                                </a>
                            </li>
                        </ul>
                      </div>

                    </div>
                    <Grid container className="dashboard-content">
                        <Grid item xs={12} className="chat-messages">
                            <div className="messages-wrapper">
                                {messages.length === 0 ? (
                                    <div className="empty-message-container">
                                        <Typography variant="body1" className="empty-message">
                                            {EMPTY_CHAT_MESSAGE}
                                        </Typography>
                                    </div>
                                ) : (
                                    messages.map((message, index) => (
                                        <div key={index} className={`chat-message ${message.role}`}>
                                            {
                                                message.role === 'assistant' &&
                                                <AiAvatar />
                                            }
                                            <Paper elevation={3} className="message-paper">
                                                <Typography
                                                    variant="body1"
                                                >
                                                    {message.content}
                                                </Typography>
                                            </Paper>
                                        </div>
                                    ))
                                )}
                                {
                                    isLoading &&
                                    <CircularProgress size={30} className="loading-spinner"/>
                                }
                            </div>
                        </Grid>
                        <Grid item xs={12} sm={10} md={10} lg={11} xl={11} className="chat-input-container">
                            <TextField
                                fullWidth
                                value={input}
                                onChange={handleInputChange}
                                onKeyPress={handleKeyPress}
                                placeholder="Type your message..."
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12} sm={2} md={2} lg={1} xl={1} className="send-button-container">
                            <Button
                                variant="contained"
                                color="primary"
                                onClick={handleSendMessage}
                                disabled={isLoading}
                                endIcon={<SendIcon />}
                            >
                                Send
                            </Button>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
            <div className="footer-container">
                <div className="footer-bold-text">Copyright © Smart Rule Engine</div>
                <div className="footer-text">All rights reserved.</div>
            </div>
        </>

    );
};

export default Dashboard;
