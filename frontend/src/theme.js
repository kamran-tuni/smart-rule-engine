import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
            main: '#113737',
        },
        error: {
            main: '#ff1744',
        },
        warning: {
            main: '#ff9800',
        },
        info: {
            main: '#2196f3',
        },
        success: {
            main: '#4caf50',
        },
        background: {
            default: '#f2f3f8',
            bright: '#ffffff',
        },
        text: {
            dark: '#212529',
            green: '#153610',
            white: '#ffffff'
        },
    },
});

export default theme;