import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM


model = Sequential()

# Add a Dense layer as the input layer
model.add(Input(input_shape = (None, 563,1))

model.add(LSTM(units=64, input_shape=(None, 563, 128), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(0.2))
model.add(LSTM(units=64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=64))

model.compile(optimizer='adam', loss='mean_squared_error')

# Print model summary
model.summary()
