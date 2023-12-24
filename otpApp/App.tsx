import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button } from 'react-native';
import { Icon } from 'react-native-elements';
import axios from 'axios';
const sendSMS = async (to) => {

let otp = ''
  const apiUrl = 'http://192.168.195.21:8000/send-sms'; // Replace with your actual FastAPI server URL

  try {
    const response = await axios.post(apiUrl, {
      to,


    });

    console.log('SMS sent successfully:', response.data.otp);
    otp = response.data.otp;
     return otp;
  } catch (error) {
    console.error('Error sending SMS:', error.response ? error.response.data : error.message);
  }

};

const isValidPhoneNumber = (phoneNumber) => {
  // Use a regular expression to validate the phone number format
  const phoneRegex = /^[0-9]{10}$/;
  return phoneRegex.test(phoneNumber);
};
const OTPLoginPage = () => {

  const [phoneNumber, setPhoneNumber] = useState('');
    const [otp, setOTP] = useState('');
    const [serverOtp, setOTPFromServer] = useState('');
    const [timer, setTimer] = useState(10);
    const [isTimerRunning, setIsTimerRunning] = useState(false);

    useEffect(() => {
      let interval;

      if (isTimerRunning) {
          interval = setInterval(() => {
            setTimer((prevTimer) => {
              if (prevTimer > 0) {
                return prevTimer - 1;
              } else {
                setIsTimerRunning(false);
                clearInterval(interval); // Clear the interval when timer hits 0
                return 0;
              }
            });
          }, 1000);
        }

        return () => clearInterval(interval);
      }, [isTimerRunning]);

    const handleStartTimer = () => {
      setIsTimerRunning(true);
      setTimer(10);
    };

    const handleResendOTP = async () => {
        try {
          const newOTP = await sendSMS(phoneNumber);
          setOTPFromServer(newOTP);
          console.log('Otp sent:', newOTP); // Log the actual OTP value
          handleStartTimer();
        } catch (error) {
          console.log('Error sending OTP:', error.message);
          // Handle the error appropriately, e.g., display an error message to the user
        }
      };


    const handleVerifyOTP = () => {
      if (otp === serverOtp) {
        // Authenticate the user and navigate to the home screen
        alert('Authentication successful!');
        // Implement navigation logic here (e.g., using React Navigation)
      } else {
        alert('Incorrect OTP. Please try again.');
        // You can display an error message to the user
      }
    };

    return (
      <View style={{ padding: 20, flex: 1, justifyContent: 'center' }}>
        <TextInput
          placeholder="Enter your phone number"
          keyboardType="phone-pad"
          value={phoneNumber}
          onChangeText={(text) =>{
           const phone = text.replace(/[^0-9]/g, '');
           setPhoneNumber(phone)
           }}
          required
          minLength={10}
        />

        <View style={{ flexDirection: 'row', marginTop: 20 }}>
          <TextInput
            placeholder="Enter OTP"
            keyboardType="numeric"
            value={otp}
            maxLength={6}
            onChangeText={(text) => {
                // Use a regular expression to allow only numeric input
                const numericText = text.replace(/[^0-9]/g, '');
                setOTP(numericText);
              }}
          />

          <Button title="Verify" onPress={handleVerifyOTP} disabled={!otp} />
        </View>

        <View style={{ flexDirection: 'row', alignItems: 'center', marginTop: 10,marginBottom:10 }}>
          <Text>Resend OTP in: {timer}s</Text>


        </View>

        {!isTimerRunning && (
          <Button title="Send OTP" onPress={handleResendOTP} disabled={!isValidPhoneNumber(phoneNumber) }/>
        )}
      </View>
    );
};

export default OTPLoginPage;
