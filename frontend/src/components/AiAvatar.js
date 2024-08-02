import React from 'react';
import { Avatar } from '@mui/material';
import { useTheme } from '@mui/material/styles';


const AiAvatar = () => {
  const theme = useTheme();

  return (
    <Avatar
      sx={{
        backgroundColor: theme.palette.primary.main,
        marginRight: '10px'
      }}
    >
      AI
    </Avatar>
  );
};

export default AiAvatar;
