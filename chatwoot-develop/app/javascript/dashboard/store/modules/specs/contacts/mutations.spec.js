import * as types from '../../../mutation-types';
import { mutations } from '../../contacts';

describe('#mutations', () => {
  describe('#SET_CONTACTS', () => {
    it('set contact records', () => {
      const state = { records: {} };
      mutations[types.default.SET_CONTACTS](state, [
        { id: 1, name: 'contact1', email: 'contact1@chatwoot.com' },
      ]);
      expect(state.records).toEqual({
        1: {
          id: 1,
          name: 'contact1',
          email: 'contact1@chatwoot.com',
        },
      });
    });
  });

  describe('#SET_CONTACT_ITEM', () => {
    it('push contact data to the store', () => {
      const state = {
        records: {
          1: { id: 1, name: 'contact1', email: 'contact1@chatwoot.com' },
        },
      };
      mutations[types.default.SET_CONTACT_ITEM](state, {
        id: 2,
        name: 'contact2',
        email: 'contact2@chatwoot.com',
      });
      expect(state.records).toEqual({
        1: { id: 1, name: 'contact1', email: 'contact1@chatwoot.com' },
        2: { id: 2, name: 'contact2', email: 'contact2@chatwoot.com' },
      });
    });
  });

  describe('#EDIT_CONTACT', () => {
    it('update contact', () => {
      const state = {
        records: {
          1: { id: 1, name: 'contact1', email: 'contact1@chatwoot.com' },
        },
      };
      mutations[types.default.EDIT_CONTACT](state, {
        id: 1,
        name: 'contact2',
        email: 'contact2@chatwoot.com',
      });
      expect(state.records).toEqual({
        1: { id: 1, name: 'contact2', email: 'contact2@chatwoot.com' },
      });
    });
  });
});
