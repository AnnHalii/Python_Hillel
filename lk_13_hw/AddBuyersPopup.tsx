import React, { useState, useEffect, FormEvent } from 'react';
import Cookies from 'js-cookie';

import eventTracking from '../../lib/analytics/eventTracking';
import { BUYERS_POPUP_COOKIE } from '../../lib/constants';
import { redirect } from '../../lib/utils';

import { MutationAddBuyers, QueryCurrentRole } from '../../store/companies/types';
import { ADD_BUYERS, GET_CURRENT_ROLE } from '../../store/companies/queries';

import Button from '../ui/Button/Button';
import Checkbox from '../ui/Checkbox/Checkbox';
import Autosuggest from '../ui/Autosuggest/Autosuggest';
import SelectedItemsList from '../ui/SelectedItemsList/SelectedItemsList';
import Popup from '../ui/Popup/Popup';
import Message from '../ui/Message/Message';
import TextShorten from '../ui/TextShorten/TextShorten';

import SupportFooter from '../SupportFooter/SupportFooter';

import { BUYERS_LIST, PRESENT_BUYERS_LIST } from './constants';

const css = require('./AddBuyersPopup.styl');

interface Props {
    isNewCompany: boolean;
    onClose: () => void;
}

const AddBuyersPopup = (props: Props) => {
    const initList: any[] = [];
    const [isSuggestionShown, toggleSuggestionShown] = useState(false);
    const [isSuccessfullyAdded, toggleSuccessfullyAdded] = useState(false);
    const [value, setValue] = useState('');
    const [suggestions, setSuggestions] = useState(BUYERS_LIST);
    const [networkList, updateList] = useState(initList);
    const [newNetworkList, updateNewList] = useState(initList);
    const [errorMessage, showErrorMessage] = useState('');

    Cookies.set(BUYERS_POPUP_COOKIE, '1', { expires: 180 });

    useEffect(() => {
        eventTracking.sendEvent('form_store_specification', 'show');
    }, []);

    const newNetworkListItems = newNetworkList.map(item => ({
        id: item.name,
        fields: [item.name],
    }));

    const handleUpdateList = () => {
        if (!value) return;
        const updatedList: string[] = [...newNetworkList, { name: value }];
        updateNewList(updatedList);
        setValue('');
        setSuggestions(BUYERS_LIST);
    };

    const handleRemoveItem = (id: string) => {
        const updatedList: string[] = newNetworkList.filter(item => item.name !== id);
        updateNewList(updatedList);
    };

    const handleChange = (inputValue: string) => {
        setValue(inputValue);

        if (!inputValue) {
            setSuggestions(BUYERS_LIST);
        } else {
            const updatedSuggestions = BUYERS_LIST.filter(
                (item: string) => item.indexOf(inputValue) !== -1,
            );
            setSuggestions(updatedSuggestions);
        }
    };

    const handleSuggestionClick = (selection: string) => {
        const updatedList: string[] = [...newNetworkList, { name: selection }];
        updateNewList(updatedList);
        setValue('');
        setSuggestions(BUYERS_LIST);
    };

    const handleCheckboxChange = (checked: boolean, value: string, edrpou: string) => {
        if (checked) {
            updateList([...networkList, { name: value, edrpou }]);
        } else {
            const updatedNewList: string[] = networkList.filter(item => item === value);
            updateList(updatedNewList);
        }
    };

    const handleSubmit = async (
        evt: FormEvent,
        name: string,
        edrpou: string,
        callback: (arg0: any) => any,
    ) => {
        evt.preventDefault();
        const buyers = [...networkList, ...newNetworkList];
        try {
            await callback({
                variables: {
                    sellerName: name,
                    sellerEdrpou: edrpou,
                    buyers,
                },
            });
            eventTracking.sendEvent('company_confirmation', '2step_specify_stores_finish');
            eventTracking.sendEvent('form_store_specification', 'add_stores');
            toggleSuccessfullyAdded(true);
        } catch (err) {
            // TODO[TK]: show real errors after implementing it on backend
            showErrorMessage('Не вдалося додати мережі');
        }
    };

    const handleClose = () => {
        props.onClose();
        redirect('/app/deals');
    };

    const renderSuggestion = (suggestion: string) => {
        return (
            <TextShorten>
                <span className={css.capitalized}>{suggestion}</span>
            </TextShorten>
        );
    };

    if (isSuccessfullyAdded) {
        return (
            <Popup active onClose={handleClose}>
                <div className={css.root}>
                    <Message size="big" type="success">
                        Ви успішно вказали мережі, з котрими ви плануєте працювати!
                    </Message>
                    <p className={css.info}>
                        Найближчим часом з вами зв’яжеться наш менеджер і допоможе налагодити <br />
                        процес із вказаними мережами.
                    </p>
                </div>
            </Popup>
        );
    }

    const title = props.isNewCompany
        ? 'Вкажіть мережі, з котрими ви плануєте працювати'
        : 'Ми прагнемо розширити можливості ваших поставок. Поновіть,' +
          ' будь ласка, інформацію про мережі, з якими бажаєте працювати';
    return (
        <Popup active title={title} onClose={props.onClose}>
            <QueryCurrentRole query={GET_CURRENT_ROLE}>
                {({ data, error }) => {
                    if (error)
                        return (
                            <Message type="error" size="small">
                                Error: {error.message}
                            </Message>
                        );
                    const company = data && data.currentRole ? data.currentRole.company : null;
                    if (!company) return null;

                    const allowedBuyers = company.allowedBuyers;
                    let remainingBuyers = PRESENT_BUYERS_LIST;
                    if (allowedBuyers) {
                        remainingBuyers = PRESENT_BUYERS_LIST.filter(
                            buyer => !allowedBuyers.includes(buyer.edrpou),
                        );
                    }
                    return (
                        <MutationAddBuyers mutation={ADD_BUYERS}>
                            {addBuyers => (
                                <form
                                    className={css.root}
                                    onSubmit={evt =>
                                        handleSubmit(evt, company.name, company.edrpou, addBuyers)
                                    }
                                >
                                    <ul className={css.list}>
                                        {remainingBuyers.length > 0 &&
                                            remainingBuyers.map(item => {
                                                return (
                                                    <li className={css.item} key={item.edrpou}>
                                                        <label className={css.checkboxWrapper}>
                                                            <Checkbox
                                                                onChange={checked => {
                                                                    handleCheckboxChange(
                                                                        checked,
                                                                        item.name,
                                                                        item.edrpou,
                                                                    );
                                                                }}
                                                            />
                                                            <figure className={css.figure}>
                                                                <figcaption
                                                                    className={css.figcaption}
                                                                >
                                                                    {item.name}
                                                                </figcaption>
                                                                <div className={css.image}>
                                                                    <img
                                                                        src={`${CONFIG.STATIC_HOST}/images/logos/${item.edrpou}.png`}
                                                                        alt={item.name}
                                                                    />
                                                                </div>
                                                            </figure>
                                                        </label>
                                                    </li>
                                                );
                                            })}
                                    </ul>
                                    <div className={css.row}>
                                        <div className={css.field}>
                                            <label className={css.label} htmlFor="network_name">
                                                Вказати інші мережі
                                            </label>

                                            <Autosuggest
                                                id={'network_name'}
                                                showSuggestions={isSuggestionShown}
                                                type={'text'}
                                                value={value}
                                                placeholder={
                                                    'Введіть назву мережі і натисніть кнопку “Додати”'
                                                }
                                                optionButtonText={
                                                    value ? `Додати "${value}"` : undefined
                                                }
                                                suggestionsData={suggestions}
                                                renderSuggestion={renderSuggestion}
                                                onSuggestionClick={handleSuggestionClick}
                                                onCloseSuggestion={() =>
                                                    toggleSuggestionShown(false)
                                                }
                                                onChange={handleChange}
                                                onFocus={() => toggleSuggestionShown(true)}
                                                onOptionButtonClick={handleUpdateList}
                                            />
                                        </div>
                                        <Button theme="blue" onClick={handleUpdateList}>
                                            Додати
                                        </Button>
                                    </div>
                                    {newNetworkList.length > 0 && (
                                        <SelectedItemsList
                                            onRemoveItem={handleRemoveItem}
                                            items={newNetworkListItems}
                                        />
                                    )}
                                    <div className={css.footer}>
                                        <div className={css.button}>
                                            <Button width="full" type="submit">
                                                Вказати мережі
                                            </Button>
                                        </div>
                                        <Message type="error" size="small">
                                            {errorMessage}
                                        </Message>
                                        <SupportFooter />
                                    </div>
                                </form>
                            )}
                        </MutationAddBuyers>
                    );
                }}
            </QueryCurrentRole>
        </Popup>
    );
};

export default AddBuyersPopup;
