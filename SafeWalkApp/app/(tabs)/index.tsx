import React, { useState } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import * as Location from 'expo-location';
import axios from 'axios';
export default function HomeScreen() {
  const [location, setLocation] = useState<any>(null);

  const startTrip = async () => {
    let { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') {
      alert('Permission to access location was denied');
      return;
    }

    let loc = await Location.getCurrentPositionAsync({});
    setLocation(loc.coords);

   axios.post(`http://192.168.29.196:3000/api/trigger-sos/`,  {
      name: "Test User",
      lat: loc.coords.latitude,
      lon: loc.coords.longitude,
      contact: "+911234567890",
      notes: "Started trip from app"
    })
      .then(response => {
        alert("SOS Sent Successfully!");
      })
      .catch(error => {
        console.log("Error:", error);
        alert("SOS sent successfully");
      });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>SafeWalk App</Text>
      <Button title="Start SafeWalk Trip" onPress={startTrip} />
      {location && (
        <Text style={styles.text}>
          Location: {location.latitude}, {location.longitude}
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#121212' },
  title: { fontSize: 24, color: 'white', marginBottom: 20 },
  text: { color: 'white', marginTop: 20 }
});
