'use strict';

angular.module('superString')
  .controller('NavbarCtrl', function ($scope, $location) {
    this.menus = [{
      'title': '首页',
      'link': '#/',
      'icon': 'fa-home',
      'menus': [
          {
              'title': '统计',
              'link': '#/'
          },
          {
              'title': '任务',
              'link': '#/'
          },
          {
              'title': '计量',
              'link': '#/'
          }
      ]
    },
    {
      'title': '计算',
      'link': '#/compute',
      'icon': 'fa-tachometer',
      'menus': [
         {
              'title': '虚拟机',
              'link': '#/'
          },
          {
              'title': '规格',
              'link': '#/'
          },
          {
              'title': '快照',
              'link': '#/'
          }
      ]
    },
    {
        'title': '存储',
        'link': '#/compute',
        'icon': 'fa-tasks',
        'menus': [
            {
              'title': '存储卷',
              'link': '#/'
            },
            {
              'title': '备份',
              'link': '#/'
            },
            {
              'title': '快照',
              'link': '#/'
            }
        ]
    },
    {
        'title': '网络',
        'link': '#/compute',
        'icon': 'fa-cloud',
        'menus': [
            {
              'title': '虚拟网络',
              'link': '#/'
            },
            {
              'title': '路由',
              'link': '#/'
            },
            {
              'title': '安全组',
              'link': '#/'
            }
        ]
    },
    {
      'title': '文档',
      'link': '#/help',
      'icon': 'fa-star',
      'menus': [
            {
              'title': '文档',
              'link': '#/'
            },
            {
              'title': '帮组中心',
              'link': '#/'
            }
      ]
    },
    {
      'title': '设置',
      'link': '#/settings',
      'icon': 'fa-gear',
      'menus': [
            {
              'title': '通知',
              'link': '#/'
            },
            {
              'title': '修改密码',
              'link': '#/'
            },
      ]
    }
    ];
    
    this.isActive = function(route) {
      return route === '#'+$location.path();
    };
  });
