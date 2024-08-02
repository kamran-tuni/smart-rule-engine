import { useState } from 'react';
import { apiEndpoints, appEndpoints } from '../config/Endpoints';

import Cookies from 'js-cookie';


const useGenerateRuleEngine = () => {
    const generateRuleEngine = async (data, setIsLoading, setMessages) => {
        try {
            const csrfToken = Cookies.get('csrftoken');
            const response = await fetch(apiEndpoints.ruleEngine, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
                credentials: 'include'
            });

            const response_data = await response.json();
            if (response.ok) {

                setIsLoading(false);
                setMessages(response_data["chat_history"]);
            } else {
                throw new Error('Failed to send message');
                window.location.href = appEndpoints.login;
            }
        } catch (error) {
            console.error('Error sending message:', error);
            window.location.href = appEndpoints.login;
        }
    };

    return { generateRuleEngine };
};

export default useGenerateRuleEngine;
