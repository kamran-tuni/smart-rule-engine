import React, { useState } from 'react';
import Cookies from 'js-cookie';
import {
    TextField,
    Button,
    CircularProgress,
    Grid,
    Box,
    Typography,
    Divider,
    Tab,
    FormControl,
    Tabs,
    InputLabel,
    Select,
    MenuItem,
} from '@mui/material';

import logoImage from '../media/logo.png';

import useLogin from '../hooks/Login';
import useSignup from '../hooks/Signup';

import './Login.css';


const Login = () => {
    const { login } = useLogin();
    const { signup } = useSignup();
    const [companyName, setCompanyName] = useState('');
    const [accountId, setAccountId] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [platform, setPlatform] = useState('');
    const [baseUrl, setBaseUrl] = useState('');
    const [apiKey, setApiKey] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [message, setMessage] = useState({'severity': 'error', 'content': ''});
    const [tabIndex, setTabIndex] = useState(0);

    const handleLogin = async (event) => {
        event.preventDefault();
        setIsLoading(true);
        setMessage({'severity': 'error', 'content': ''});

        const loginData = {
            username,
            password,
        };


        login(accountId, loginData, setIsLoading, setMessage);
    };

    const handleSignup = async (event) => {
        event.preventDefault();
        setIsLoading(true);
        setMessage({'severity': 'error', 'content': ''});

        const signupData = {
            company_name: companyName,
            account_id: accountId,
            username,
            password,
            platform,
            base_url: baseUrl,
            api_key: apiKey
        };

        signup(signupData, setIsLoading, setMessage, setTabIndex)
    };

    const handleTabChange = (event, newValue) => {
        setTabIndex(newValue);
    };

    return (
        <Grid container className="grid-container">
            <Grid item xs={12} sm={12} md={8} lg={8} xl={8} className="logo-container">
                <Box style={{ textAlign: 'center' }}>
                    <img
                        src={logoImage}
                        alt="Smart Rule Engine Logo from logo.com"
                        className="login-logo"
                    />
                </Box>
            </Grid>
            <Divider orientation="vertical" flexItem />
            <Grid item  xs={12} sm={12} md={3} lg={3} xl={3}  className="form-container">
                <Box style={{ width: '80%'}}>
                    <Tabs value={tabIndex} onChange={handleTabChange} centered>
                        <Tab label="Login" />
                        <Tab label="Signup" />
                    </Tabs>
                    {tabIndex === 0 && (
                        <Box>
                            <Typography
                                variant="h6"
                                component="h1"
                                mt={4}
                                gutterBottom
                            >
                                Login
                            </Typography>
                            <form onSubmit={handleLogin}>
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Account ID"
                                    value={accountId}
                                    onChange={(e) => setAccountId(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Username"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Password"
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <Button
                                    type="submit"
                                    fullWidth
                                    variant="contained"
                                    disabled={isLoading}
                                    sx={{ mt: 3, mb: 2, height: 48, padding: '10px 0' }}
                                >
                                    {isLoading ? <CircularProgress size={24} /> : "Sign In"}
                                </Button>
                                {
                                    message.content &&
                                    <Typography
                                        color={message.severity}
                                    >
                                        {message.content}
                                    </Typography>}
                            </form>
                        </Box>
                    )}
                    {tabIndex === 1 && (
                        <Box>
                            <Typography
                                variant="h6"
                                component="h1"
                                mt={4}
                                gutterBottom
                            >
                                Account Information
                            </Typography>
                            <form onSubmit={handleSignup}>
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Company Name"
                                    value={companyName}
                                    onChange={(e) => setCompanyName(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Account ID"
                                    value={accountId}
                                    onChange={(e) => setAccountId(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Username"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Password"
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <Typography
                                    variant="h6"
                                    component="h1"
                                    mt={4}
                                    gutterBottom
                                >
                                    Platform Integration
                                </Typography>
                                <FormControl fullWidth margin="normal" required>
                                    <InputLabel>Platform</InputLabel>
                                    <Select
                                        value={platform}
                                        onChange={(e) => setPlatform(e.target.value)}
                                        label="Platform"
                                    >
                                        <MenuItem value="thingsboard">ThingsBoard</MenuItem>
                                    </Select>
                                </FormControl>
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="Base URL"
                                    value={baseUrl}
                                    onChange={(e) => setBaseUrl(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <TextField
                                    fullWidth
                                    variant="outlined"
                                    label="API Key"
                                    value={apiKey}
                                    onChange={(e) => setApiKey(e.target.value)}
                                    margin="normal"
                                    required
                                />
                                <Button
                                    type="submit"
                                    fullWidth
                                    variant="contained"
                                    disabled={isLoading}
                                    sx={{ mt: 3, mb: 2, height: 48, padding: '10px 0' }}
                                >
                                    {isLoading ? <CircularProgress size={24} /> : "Sign Up"}
                                </Button>
                                {
                                    message.content &&
                                    <Typography
                                        color={message.severity}
                                    >
                                        {message.content}
                                    </Typography>
                                }
                            </form>
                        </Box>
                    )}
                </Box>
            </Grid>
        </Grid>
    );
};

export default Login;
