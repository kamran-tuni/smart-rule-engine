import { useState } from 'react';
import { apiEndpoints, appEndpoints } from '../config/Endpoints';

import Cookies from 'js-cookie';


const useLogout = () => {
    const logout = async (data) => {
        try {
            const csrfToken = Cookies.get('csrftoken');
            const response = await fetch(apiEndpoints.logout, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
            });

            if (response.ok) {
                console.log(appEndpoints.login)
                window.location.href = appEndpoints.login;
            } else {
                console.error('Failed to log out');
                window.location.href = appEndpoints.login;
            }
        } catch (error) {
            console.error('Error logging out:', error);
        }
    };

    return { logout };
};

export default useLogout;
