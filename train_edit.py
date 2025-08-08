import pandas as pd

train_df = pd.read_csv(("C:/Users/apria/Project/Programming_Python/git_spaceship_machineLearning/Data/train.csv"))

train_df['Age'] = train_df['Age'].fillna(round(train_df['Age'].mean()))

zero_list = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
for i in zero_list:
    train_df[i] = train_df[i].fillna(0)
    
train_df = train_df.dropna()

#print(train_df.isnull().any())

drop_list = ['HomePlanet', 'Destination', 'Cabin', 'Name']
train_df = train_df.drop(drop_list, axis=1)

category_list = ['CryoSleep', 'VIP', 'Transported']
for i in category_list:
    train_df[i] = train_df[i].astype('category').cat.codes