// import React from 'react';
// const UserContext = () =>{
//     return <div>User Context</div>
// }

// export default UserContext;

import React, { createContext, useState } from "react";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null); // or initialize with user data if stored in localStorage

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
};
