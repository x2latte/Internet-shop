import { Outlet, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Drawer, List, ListItem, ListItemIcon, ListItemText, Box } from '@mui/material';
import { Inventory, Category, BrandingWatermark, ShoppingCart } from '@mui/icons-material';

const drawerWidth = 240;

export default function Layout() {
  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography variant="h6" noWrap component="div">
            Admin Panel
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer variant="permanent" sx={{ width: drawerWidth, flexShrink: 0 }}>
        <Toolbar />
        <Box sx={{ overflow: 'auto' }}>
          <List>
            <ListItem button component={Link} to="/orders">
              <ListItemIcon><ShoppingCart /></ListItemIcon>
              <ListItemText primary="Orders" />
            </ListItem>
            <ListItem button component={Link} to="/products">
              <ListItemIcon><Inventory /></ListItemIcon>
              <ListItemText primary="Products" />
            </ListItem>
            <ListItem button component={Link} to="/categories">
              <ListItemIcon><Category /></ListItemIcon>
              <ListItemText primary="Categories" />
            </ListItem>
            <ListItem button component={Link} to="/brands">
              <ListItemIcon><BrandingWatermark /></ListItemIcon>
              <ListItemText primary="Brands" />
            </ListItem>
          </List>
        </Box>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        <Outlet />
      </Box>
    </Box>
  );
}