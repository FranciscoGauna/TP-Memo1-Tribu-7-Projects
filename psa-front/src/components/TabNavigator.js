import React, { useState } from 'react';

const TabNavigator = ({
    tabs,
    contents
}) => {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  const renderTabs = () => {
    return tabs.map((tab, index) => (
      <div
        key={index}
        className={`tab ${activeTab === index ? 'active' : ''}`}
        onClick={() => handleTabClick(index)}
      >
        {tab}
      </div>
    ));
  };

  const renderContent = () => {
    return <div className="content">{contents[activeTab]}</div>;
  };

  return (
    <div>
      <div className="tab-container">{renderTabs()}</div>
      {renderContent()}
    </div>
  );
};

export default TabNavigator;