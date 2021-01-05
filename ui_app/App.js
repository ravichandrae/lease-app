import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Alert, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

function UserSignupScreen({ navigation }) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  return (
    <View style={styles.container}>
       <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Name"
            placeholderTextColor="#003f5c"
            onChangeText={(name) => setName(name)}
        />
       </View>
       <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Phone"
            placeholderTextColor="#003f5c"
            onChangeText={(phone) => setPhone(phone)}
          />
        </View>
        <TouchableOpacity style={styles.loginBtn} onPress={()=>{signupUser(name, phone)}}>
         <Text style={styles.loginText}>Signup</Text>
        </TouchableOpacity>
    </View>
  );
}

function signupUser(name, phone) {
  console.log(name + phone);
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ "mobile": phone, "name": name })
  };
  fetch('http://127.0.0.1:8000/users', requestOptions)
        .then(response => response.json())
        .then(data => console.log(JSON.stringify(data)));
}

function ProviderSignupScreen({ navigation }) {
  const [phone, setPhone] = useState("");
  const [name, setName] = useState("")
  return (
    <View style={styles.container}>
       <View style={styles.inputView}>
       <TextInput
          style={styles.TextInput}
          placeholder="Name"
          placeholderTextColor="#003f5c"
          onChangeText={(name) => setName(name)}
        />
        </View>
        <View style={styles.inputView}>
       <TextInput
          style={styles.TextInput}
          placeholder="Phone"
          placeholderTextColor="#003f5c"
          onChangeText={(phone) => setPhone(phone)}
        />
        </View>
        <Button
        title="Signup"
        onPress={() => console.log("Signup")}
      />
    </View>
  );
}

function UserScreen({ navigation }) {
  const [phone, setPhone] = useState("");
  return (
    <View style={styles.container}>
      <View style={styles.inputView}>
       <TextInput
          style={styles.TextInput}
          placeholder="Phone"
          placeholderTextColor="#003f5c"
          onChangeText={(phone) => setPhone(phone)}
        />
      </View>
      <Button
        title="Signup"
        onPress={() => navigation.navigate('UserSignupScreen')}
      />
    </View>
  );
}

function ProviderScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={styles.inputView}>
        <TextInput
            style={styles.TextInput}
            placeholder="Phone."
            placeholderTextColor="#003f5c"
            onChangeText={(phone) => setPhone(phone)}
          />
      </View>
      <Button
        title="Signup"
        onPress={() => navigation.navigate('ProviderSignupScreen')}
        />
    </View>
  );
}

function SplashScreen({ navigation }) {
    return(
      <View style={styles.container}>
        <View style={styles.inputView}>
          <Button
            title="Login as User"
            onPress={() => navigation.navigate('UserScreen')}
          />
        </View>
        <View style={styles.inputView}>
          <Button
            title="Login as Provider"
            onPress={() => navigation.navigate('ProviderScreen')}
          />
        </View>
      </View>
    );
}

const Stack = createStackNavigator();

export default function App() {
  return(
    <NavigationContainer>
       <Stack.Navigator>
        <Stack.Screen name="SplashScreen" component={SplashScreen} />
        <Stack.Screen name="UserScreen" component={UserScreen} />
        <Stack.Screen name="ProviderScreen" component={ProviderScreen} />
        <Stack.Screen name="UserSignupScreen" component={UserSignupScreen} />
        <Stack.Screen name="ProviderSignupScreen" component={ProviderSignupScreen} />
      </Stack.Navigator>
    </NavigationContainer>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputView: {
    backgroundColor: "#FFC0CB",
    borderRadius: 30,
    width: "70%",
    height: 45,
    marginBottom: 20,
 
    alignItems: "center",
  },
  TextInput: {
    height: 50,
    flex: 1,
    padding: 10,
    margin: 15,
  },
  loginBtn: {
    width: "80%",
    borderRadius: 25,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 40,
    backgroundColor: "#FF1493",
  },
});
